import scala.collection.mutable

object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        val numIndices = mutable.HashMap[Int, Int]()
        
        for( (num, index) <- nums.zipWithIndex ) {
            val complement = target - num
            if(numIndices.contains(complement)) {
                return Array(numIndices(complement), index)
            } 
            numIndices(num) = index
        }
        throw new Exception("exception")
    }
}