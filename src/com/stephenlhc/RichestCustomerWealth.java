package com.stephenlhc;

public class RichestCustomerWealth {
    // 1672. Richest Customer Wealth
    public int maximumWealth(int[][] accounts) {
        int max = Integer.MIN_VALUE;
        for (int[] account : accounts) {
            int sum = 0;
            for (int j = 0; j < accounts[0].length; j++)
                sum += account[j];

            max = Math.max(sum, max);
        }
         return max;
    }
}
