// Returns sum of arr[0..index].
// This function assumes that the array has been preprocessed and
// partial sums of the array elements are already available in the
// BITree
const getSum =
  (BITree, index) => { 
    let sum = 0
  
    // Find sum of all ancestors of the current node
    while (index > 0) { 
      sum += BITree[index]        // Increment sum by current node value
      index -= index & (-index)   // Get index of ancestor node
    } 

    return sum
  } 

// Updates a node in the Binary Index Tree at a given index
// Argument 'val' is added to BITree[index] and all of its successors
const updateBIT =
  (BITree, index, n, val) => { 
    // Update all successors of BITree[index]
    while (index <= n) { 
      BITree[index] += val       // Add 'val' to current node of BI Tree 
      index += index & (-index)  // Get index of successor node
    }

    return BITree
  } 

const getInvCount =
  arr =>
    (maxEl => 
      // Traverse all the array elements from right to left
      arr.reduceRight(
        (accObj, el) => ({
          count : accObj.count + getSum(accObj.BIT, el - 1)
          , BIT : updateBIT(accObj.BIT, el, maxEl, 1)
        })
        // Use an accumulator object that holds both the inversion
        // count and the Binary Index Tree with maxEl+1 elements, all
        // initialised to zero
      , {count : 0, BIT : Array(maxEl+1).fill(0)}
      // Return how many inversion were needed
      ).count
    )
    // Find the maximum element in the array and pass value this as an
    // argument to the anonymous function above
    (arr.reduce((maxVal, el) => el > maxVal ? el : maxVal, -Number.MAX_SAFE_INTEGER))

// Complete the insertionSort function below.
function insertionSort(arr) {
  return getInvCount(arr)
}