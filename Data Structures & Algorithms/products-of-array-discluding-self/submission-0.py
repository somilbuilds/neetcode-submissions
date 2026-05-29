class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # follow up answer 
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer


        # my answer brute force:
        # ans=[]
        # for num in nums:
        #     pros=1
        #     for i in nums:
        #         if i==num:
        #             continue
        #         pros*=i
        #     ans.append(pros)
        # return ans

# # GPT zero division answer:
#         class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         zero_count = 0
#         product = 1

#         for num in nums:
#             if num == 0:
#                 zero_count += 1
#             else:
#                 product *= num

#         ans = []

#         for num in nums:

#             if zero_count > 1:
#                 ans.append(0)

#             elif zero_count == 1:

#                 if num == 0:
#                     ans.append(product)
#                 else:
#                     ans.append(0)

#             else:
#                 ans.append(product // num)

#         return ans










