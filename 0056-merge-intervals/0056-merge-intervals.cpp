class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        int n = intervals.size();
        sort(intervals.begin(), intervals.end());
        // for (int i=0;i<n;i++){
        //     for (int j=i+1;j<n;j++){
        //         if (intervals[i][0]>intervals[j][0]){
        //             vector<int> arr;
        //             arr = intervals[i];
        //             intervals[i] = intervals[j];
        //             intervals[j] = arr;
        //         }
        //     }
        // }
        vector<vector<int>> ans;
        ans.push_back(intervals[0]);
        for (int i=1;i<n;i++){
            if (ans.back()[1]<intervals[i][0]){
                ans.push_back(intervals[i]);
            }
            else{
                ans.back()[1]=max(intervals[i][1],ans.back()[1]);    
            }
            
        }
        return ans;
    }
};