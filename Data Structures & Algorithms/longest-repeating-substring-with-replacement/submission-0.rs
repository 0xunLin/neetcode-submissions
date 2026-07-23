impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();

        let mut left = 0;
        let mut freq = [0;26]; // Tracks counts of uppercase letters A-Z
        let mut max_freq = 0;
        let mut best = 0;

        for right in 0..bytes.len() {
            let right_index = (bytes[right]-b'A') as usize;
            freq[right_index] += 1;

            max_freq = max_freq.max(freq[right_index]);

            if ((right-left+1) as i32) - max_freq > k {
                let mut left_index = (bytes[left]-b'A') as usize;
                freq[left_index] -= 1;
                left += 1;

            }
            best = best.max(right-left+1)

        }
        best as i32
    }
}
