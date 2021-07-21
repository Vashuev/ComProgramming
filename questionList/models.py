from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionList(models.Model):
    """
    models storing information about Questions from leetcode, fields are
        question : url for a particular question
        topic : like array, heap, stack etc
        level : Easy, Medium, Hard
        tutorial: any reference for solution outside the Leetcode, like Youtube link 
    """

    TOPICS = [
        ('array', 'Arrays'),
        ('dp', 'Dynamic Programing'),
        ('string', 'Strings'),
        ('maths', 'Maths'),
        ('greedy', 'Greedy'),
        ('dfs', 'DFS'),
        ('tree', 'Tree'),
        ('hash table', 'Hash Table'),
        ('binary search', 'Binary Search'),
        ('bfs', 'BFS'),
        ('two pointer', 'Two Pointer'),
        ('backtracking', 'BackTracking'),
        ('stack', 'Stack'),
        ('design', 'Design'),
        ('graph', 'Graph'),
        ('bit', 'Bit Manipulation'),
        ('linked list', 'Linked List'),
        ('heap', 'HEAP'),
        ('sliding window', 'Sliding Window'),
        ('trie', 'trie'),
        ('segment tree', 'Segment Tree')
    ]

    LEVELS = [
        ('E', 'Easy'),
        ('M', 'Medium'),
        ('H', 'Hard'),
    ]

    question = models.CharField(max_length=100)
    topic = models.CharField(max_length=15, choices= TOPICS)
    level = models.CharField(max_length=1, choices= LEVELS)
    tutorial = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        parts = self.question.split('/')
        return parts[-2]


class QueDoneByUser(models.Model):
    """
        This model store all question done by individual user, 
        Many to Many relationship between Questions and User
    """

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    questionlist = models.ManyToManyField(QuestionList)

    def __str__(self):
        return str(self.owner ) + str(self.owner.id)
