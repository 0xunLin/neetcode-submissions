impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let bytes = s.as_bytes();

        let mut char_index = [0_usize;128];

        let mut left = 0;
        let mut max_len = 0;

        for right in 0..bytes.len() {
            let char_bytes = bytes[right] as usize; //expand

            /*repair*/
            left = left.max(char_index[char_bytes]);
            char_index[char_bytes] = right+1;

            max_len = max_len.max(right-left+1); //record
        } 
        max_len as i32
    }
}
