impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;

        let mut leftMax = 0;
        let mut rightMax = 0;

        let mut total = 0;

        while left<right {
            if height[left]<height[right] {
                if height[left]>=leftMax {
                    leftMax = height[left];
                } else {
                    total += leftMax - height[left];
                }
                left += 1;
            } else {
                if height[right]>=rightMax {
                    rightMax = height[right];
                } else {
                    total += rightMax - height[right];
                }
                right -= 1;
            }
        }

        total
    }
}
