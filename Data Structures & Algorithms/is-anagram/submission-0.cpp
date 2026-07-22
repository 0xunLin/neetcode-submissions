class Solution {
public:
    bool isAnagram(string s, string t) {
        std::string newS = s;
        std::string newT = t;

        std::sort(newS.begin(), newS.end());
        std::sort(newT.begin(), newT.end());

        return newS == newT;
    }
};
