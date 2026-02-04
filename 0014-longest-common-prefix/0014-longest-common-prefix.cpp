class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string s;
        int minn = INT_MAX;
        for (string i:strs){
            minn = min(minn,int(i.size()));
        }
        if (strs.empty()) return "";
        for (int i=0;i<minn;i++){
            char a = strs[0][i];
            for (string c:strs){
                if (c[i] != a){
                    return s;
                }
            }
            s.push_back(a);
        }
        return s;

    }
};