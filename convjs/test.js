var nj = require('numjs');
var block = nj.array([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0,0]])
var kernel = nj.ones([3, 3])
function convolve(input, kernel){
  let ix = input.shape[0];
  let iy = input.shape[1];
  let kx = kernel.shape[0];
  let ky = kernel.shape[1];
  let padded_input = nj.zeros([ix + (kx - 1) * 2, iy + (ky - 1) * 2]);
  
  // Padding input
  padded_input.slice([kx - 1, kx - 1 + ix], [ky - 1, ky - 1 + iy]).assign(input, false)
  // console.log(padded_input.toString())
  let out = nj.convolve(padded_input, kernel);
  
  return out;
}


let n_neibours  = convolve(block, kernel).slice([1,-1],[1,-1]).subtract(block)
console.log(n_neibours.toString())
next = block.clone()
console.log(next.toString())