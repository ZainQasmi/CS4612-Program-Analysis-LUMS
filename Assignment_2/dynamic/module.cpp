#include "llvm/Support/DataTypes.h"
#include "llvm/Support/raw_ostream.h"
#include <iostream>
#include <cstdio>
#include <map>
#include <string>

using namespace std;
using namespace llvm;

map <string, int> dInstructionCount;

void counter(char * OpcodeName, int count) {
  string iName = OpcodeName;

  if (dInstructionCount[iName] == 0) {
    dInstructionCount[iName] = count;
  } else {
    dInstructionCount[iName] = dInstructionCount[iName] + count;
  }
}

void printer() {
  int totalCount = 0;
  for (std::map<string,int>::iterator it=dInstructionCount.begin(); it!=dInstructionCount.end(); ++it){
     errs() << it->first << "\t\t" << it->second << "\n";
     totalCount = totalCount + it->second;
  }
  errs() << "Total" << "\t\t" <<totalCount << "\n";
}



// Append this to command line -D__STDC_CONSTANT_MACROS -D__STDC_LIMIT_MACROS



