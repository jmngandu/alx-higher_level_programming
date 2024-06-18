#!/usr/bin/node
// Executes theFunction 'x' times
exports.callMeMoby = function (x, theFunction) {
  while (x-- > 0) {
    theFunction();
  }
};
