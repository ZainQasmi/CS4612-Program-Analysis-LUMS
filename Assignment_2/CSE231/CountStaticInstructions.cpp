#include "llvm/Pass.h"
#include "llvm/IR/Function.h"
#include "llvm/IR/Module.h"
#include "llvm/Support/raw_ostream.h"
#include "llvm/Support/InstIterator.h"
#include <iostream>
#include <map>
// #include "llvm/IR/Value.h"

using namespace std;
using namespace llvm;

namespace {
	struct staticCount : public ModulePass {
		static char ID;
		staticCount() : ModulePass(ID) {}

		int counter = 0;
		std::map<string, int> iCount;

		// string iName;
		// std::cout << "lol" << std::endl;

		bool runOnModule(Module &M) override {
			Module::iterator MI = M.begin(), ME = M.end();
			for (; MI != ME; ++MI ) {
				for (inst_iterator I = inst_begin(MI), E = inst_end(MI); I != E; ++I){
					counter++;
					string iName = Instruction::getOpcodeName(I->getOpcode());
					// errs() << "name: " << iName;
					if (iCount[iName] == 0) {
						iCount[iName] = 1;
					} else {
						iCount[iName]++;
					}
					// I->getOpcode();
					// errs() << *I << "\n";
				}
			}

			for (std::map<string,int>::iterator it=iCount.begin(); it!=iCount.end(); ++it){
			   // std::cout << it->first << " => " << it->second << '\n';
			   errs() << it->first << "\t\t" << it->second << "\n";
			}
			errs() << "Total" << "\t\t" <<counter << "\n";

			// errs() << "Hello: ";
			// errs().write_escaped(F.getName()) << '\n';
			return false;
		}

		// void print(raw_ostream &OS, const Module * M) const {
		// 	OS << "Total " << counter << "\n";
		// }



	}; // end of struct staticCount
}  // end of anonymous namespace

char staticCount::ID = 0;

static RegisterPass<staticCount> X("staticCount", "Static Count Instructions",
														 false /* Only looks at CFG */,
														 false /* Analysis Pass */);