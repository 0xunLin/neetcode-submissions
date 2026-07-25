impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        // Filter out non-alphanumeric chars and normalize to lowercase
        let clean_chars = s.chars()
            .filter(|c| c.is_ascii_alphanumeric())
            .map(|c| c.to_ascii_lowercase());

        // Compare the iterator with its reversed version
        clean_chars.clone().eq(clean_chars.rev())
    }
}
