class Solution {
public:
    string largestGoodInteger(string num) {
        string ans = "-1";
        for (int i = 0; i < num.length() - 2; ++i) {
            string curr = num.substr(i, 1);
            for (int j = i + 1; j < i + 3; ++j) {
                if (num[j] != num[i]) {
                    break;
                }
                curr += num[i];
            }
            if (curr.length() == 3 && stoi(curr) > stoi(ans)) {
                ans = curr;
            }
        }
        if (ans == "-1") {
            return "";
        }
        return ans;        
    }
};

