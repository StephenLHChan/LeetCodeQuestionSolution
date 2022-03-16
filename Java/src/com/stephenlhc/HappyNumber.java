package com.stephenlhc;

import java.util.HashSet;
import java.util.Set;

public class HappyNumber {
    // 202. Happy Number
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        return isHappy(n, seen);
    }

    private boolean isHappy(int n, Set seen){
        if(n == 1) return true;
        if(seen.contains(n)) return false;

        seen.add(n);

        int sum = 0;
        while (n != 0){
            sum += (n % 10) * (n % 10);
            n /= 10;
        }

        return isHappy(sum, seen);
    }
}
