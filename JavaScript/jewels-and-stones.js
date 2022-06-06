// 771. Jewels and Stones

var numJewelsInStones = function(jewels, stones) {
    const set = new Set(jewels)
    return stones.split('').reduce((res, s) => {
        res + set.has(s)}
        , 0)
};