class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxx = 0;
        unordered_set<char> sett;
        int left = 0;
        for (int right=0;right<s.size();right++){
            while (sett.find(s[right])!=sett.end()){
                sett.erase(s[left]);
                left++;
            }
            sett.insert(s[right]);
            maxx = max(maxx,int(sett.size()));
        }
        return maxx;
    }
};