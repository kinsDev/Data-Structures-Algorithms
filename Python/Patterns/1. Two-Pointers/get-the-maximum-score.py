def maxSum(nums1, nums2):
    pointer1, pointer2 = 0, 0
    len1, len2 = len(nums1), len(nums2)
    sum_path1, sum_path2 = 0, 0
    MOD = 10 ** 9 + 7

    while pointer1 < len1 or pointer2 < len2:
        if pointer1 < len1 and (pointer2 == len2 or nums1[pointer1] < nums2[pointer2]):
            sum_path1 += nums1[pointer1]
            pointer1 += 1

        elif pointer2 < len2 and (pointer1 == len1 or nums1[pointer1] > nums2[pointer2]):
            sum_path2 += nums2[pointer2]
            pointer2 += 1

        else:
            sum_path1 = sum_path2 = max(sum_path1, sum_path2) + nums1[pointer1]
            pointer1 += 1
            pointer2 += 1

    return max(sum_path1, sum_path2) % MOD

"""
The goal is to collect the maximum score by traversing two sorted arrays where switching between them is only allowed at common elements. The challenge is to choose when to switch to maximize the cumulative score.

This is done efficiently using the two pointers technique, which allows simultaneous traversal of both arrays in linear time, without the need to build or store all possible paths. As the arrays are strictly increasing, any prefix sum is guaranteed to grow as we move forward. At each common element, we are allowed to switch arrays. We decide whether to switch by comparing the scores accumulated from both paths and choosing the larger one as the new base to continue forward. This decision ensures that we always continue on the more rewarding path, step by step.

This approach works reliably because, beyond any common element, both arrays are still strictly increasing. So, regardless of which array we continue from, the score will continue to grow. We guarantee that the optimal path is preserved by always choosing the higher cumulative score at a common value. Let’s take an example to further understand this:

nums1 
=
[
10
,
20
,
40
,
50
,
60
]
=[10,20,40,50,60]

nums2 
=
[
1
,
2
,
40
,
10000
,
35000
]
=[1,2,40,10000,35000]

At the first common element 
40
40
, we compare the cumulative sums collected so far:

From sum_path1: 
10
+
20
=
30
10+20=30

From sum_path2: 
1
+
2
=
3
1+2=3

As 
30
>
3
30>3
, we take the maximum sum_path1 sum and add the common value 
40
40
 to get 
70
70
, then assign this to both paths, sum_path1 and sum_path2. This synchronization means both paths now carry the same score forward, ensuring we don’t miss high-value segments in either array, like nums2 having 
10000
10000
 next. The higher-sum path will naturally take the lead. Once both arrays are fully processed, we simply return the greater of the two running totals. This method avoids generating every possible path and instead builds the optimal one on-the-fly in linear time, making it both elegant and efficient.

Now, let’s look at the solution steps below:

Initialize two pointers, pointer1 and pointer2, to traverse nums1 and nums2, respectively.

Initialize two running sums, sum_path1 and sum_path2, to track the current total score on each path.

Define a constant MOD = 10^9 + 7 to apply modulo as required by the problem constraints to prevent overflow.

Traverse both arrays simultaneously using the two pointers, continuing until both pointers have reached the end of their respective arrays:

If nums1[pointer1] 
<
<
 nums2[pointer2]:

Add nums1[pointer1] to sum_path1 and increment pointer1.

Else if nums1[pointer1] 
>
>
 nums2[pointer2]:

Add nums2[pointer2] to sum_path2 and increment pointer2.

Else (if nums1[pointer1] 
=
=
==
 nums2[pointer2] (common element):

Add the common value to the maximum of sum_path1 and sum_path2.

Assign this computed sum to both sum_path1 and sum_path2 to synchronize paths.

Increment both pointers to move past the common value in both arrays.

After traversal, take the maximum of sum_path1 and sum_path2.

Return the result modulo 10^9 + 7
"""