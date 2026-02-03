class Solution {
public:
    bool isValid(string s) {
        unordered_set<char> open = {'(','{','['};
        unordered_map<char,char> dict = {
            {')', '('},
            {'}', '{'},
            {']', '['}
        };
        stack<char> st;
        char x;
        for (char c:s){
            if (open.find(c) != open.end()){
                st.push(c);
            }
            else{
                if (st.empty()) return false;
                x = st.top();
                st.pop();
                if (dict[c] != x){
                    return false;
                }
            }
        }
        return st.empty();
    }
};