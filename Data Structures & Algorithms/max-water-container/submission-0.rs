impl Solution {
    pub fn max_area(heights: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = heights.len() - 1;

        let mut max = 0;

        while left<right {
            let area: i32 = ((right as i32) - (left as i32)) * (heights[left].min(heights[right]));

            if area>max {
                max = area;
            } else {
                if heights[left]==heights[right] {
                    left += 1;
                    right -= 1;
                } else if heights[left]<heights[right] {
                    left += 1;
                } else {
                    right -= 1;
                }
            }
        }

        max as i32
    }
}
