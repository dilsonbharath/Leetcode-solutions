/**
 * @param {string[]} words
 * @param {string} s
 * @return {boolean}
 */
var isAcronym = function(words, s) {
    let a=words.length
    let b=s.length
    if (words.length !== s.length) {
        return false;
    }
    for (i=0;i<a;i++){
        if (words[i]=='' || words[i][0]!==s[i]){
            return false;
        }
    }
    return true;
};