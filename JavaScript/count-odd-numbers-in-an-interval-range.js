// 1523. Count Odd Numbers in an Interval Range

var countOdds = function(low, high) {
    const additionalOne = (low % 2 === 1 || high % 2 === 1) ? 1: 0;
    return Math.floor((high - low) / 2) + additionalOne;
};