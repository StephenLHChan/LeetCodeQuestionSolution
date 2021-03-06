package com.stephenlhc;

public class CountOddNumbersInAnIntervalRange {
    // 1523. Count Odd Numbers in an Interval Range
    public int countOdds(int low, int high) {
        if (low % 2 == 1 || high % 2 == 1)
            return (high - low) / 2 + 1;
        return ((high - low) / 2);
    }
}
