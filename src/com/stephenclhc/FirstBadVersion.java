package com.stephenclhc;

public class FirstBadVersion {
    //278. First Bad Version

    /* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

    public int firstBadVersion(int n) {

        int left = 1;
        int right = n;

        int middle = 0;
        while (left < right) {
            middle = (left + right) / 2; // It is better to code -> middle = left + (right - left) / 2

            if (isBadVersion(middle))
                right = middle;
            else left = middle + 1;
        }
        return left;

    }
}