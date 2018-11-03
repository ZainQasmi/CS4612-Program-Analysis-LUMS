#include "llvm/Pass.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Module.h"
#include "llvm/IR/Instruction.h"
#include "llvm/Support/InstIterator.h"
#include "llvm/IR/BasicBlock.h"
#include "llvm/ADT/Statistic.h"
#include "llvm/IR/IRBuilder.h"
// #include "llvm/IR/Value.h"
#include <iostream>
#include <map>

using namespace std;
using namespace llvm;

// To insert calls to a function, you will find the following functions useful:
//     Module::getOrInsertFunction
//     IRBuilder::CreateCall
//     FunctionType::get

string modFun1("_Z7counterPci"); //counter function name in module.ll
string modFun2("_Z7printerv"); //printer function name in module.ll

namespace {
    struct dynamicCount : public ModulePass {
        static char ID;
        dynamicCount() : ModulePass(ID) {}

        // int counter = 0;
        // std::map<string, int> iCount;
        // string iName;
        // std::cout << "lol" << std::endl;

        virtual bool runOnModule(Module &M){
            //Pointers to functions
            Function *counterFunction = cast<Function> (M.getOrInsertFunction("modFun1",Type::getVoidTy(M.getContext()),Type::getInt8PtrTy(M.getContext()),Type::getInt32Ty(M.getContext()),NULL));
            Function *printFunction = cast<Function> (M.getOrInsertFunction("modFun2",Type::getVoidTy(M.getContext()),NULL));
            // iterate over Modules
            for (Module::iterator FI = M.begin(), FE = M.end(); FI != FE; FI++){
                // iterate over Basic Blocks
                for(Function::iterator BB = FI->begin(), E = FI->end(); BB != E; ++BB){
                    // iterate over functions and count each instruction
                    map<string, int> iCount;
                    for (BasicBlock::iterator it = BB->begin(), IE = BB->end(); it != IE; it++){
                        Instruction * _it = &*it;
                        string iName = Instruction::getOpcodeName(_it->getOpcode());
                        if (iCount[iName] == 0){
                            iCount[iName] = 1;
                        }
                        else {
                            iCount[iName]++;
                        }
                    }

                    IRBuilder<> builder(BB);
                    BasicBlock::iterator iteratorBB = BB->end();
                    iteratorBB--;
                    builder.SetInsertPoint(iteratorBB);

                    map <string, int>::const_iterator iter;
                    for (iter = iCount.begin(); iter != iCount.end(); iter++){
                        Value *_iName = builder.CreateGlobalStringPtr(iter->first);
                        Value *_iCount = ConstantInt::get(Type::getInt32Ty(M.getContext()), iter->second);
                        builder.CreateCall2(counterFunction, _iName, _iCount);
                    }
                }

                // inserting print just before executable exists
                if ((*FI).getName() == "main" ) {
                    Function::iterator BB = FI->end();
                    BB--;
                    // setting IR insert point at the end of main
                    IRBuilder<> builder(BB);
                    BasicBlock::iterator endMain = BB->end();
                    endMain--;
                    builder.SetInsertPoint(endMain);
                    builder.CreateCall (printFunction, "");
                }
            }

            // for (std::map<string,int>::iterator it=iCount.begin(); it!=iCount.end(); ++it){
            //    // std::cout << it->first << " => " << it->second << '\n';
            //    errs() << it->first << "\t\t" << it->second << "\n";
            // }
            // errs() << "Total" << "\t\t" <<counter << "\n";
            
            return true;
        }

        // int totalCount = 0;
        // for (std::map<string,int>::iterator it=dInstructionCount.begin(); it!=dInstructionCount.end(); ++it){
        //    errs() << it->first << "\t\t" << it->second << "\n";
        //    totalCount = totalCount + it->second;
        // }
        // errs() << "Total" << "\t\t" <<totalCount << "\n";
    }; // end of struct dynamicCount
}  // end of anonymous namespace

char dynamicCount::ID = 0;

static RegisterPass<dynamicCount> X("dynamicCount", "Dynamic Count Instructions",
                                                         false /* Only looks at CFG */,
                                                         false /* Analysis Pass */);