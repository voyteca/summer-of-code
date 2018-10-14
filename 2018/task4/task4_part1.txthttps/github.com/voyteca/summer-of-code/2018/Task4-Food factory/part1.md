There is a lot of food to prepare and cook for the barbeque. You need to make sure you have enough time to do all the work before the guests arrive.

The tasks to be performed are listed in 04-preparation.txt. There's one task per line. Each line starts with the one-word name for that task, followed by the time that task takes, and finally the names of all the tasks it depends on.

For instance, here's a summary of eight tasks you have to do:

quesadilla 18
asparagus 12 tuna barley
barley 20
linguine 20 quesadilla barley
parsnip 20
kingfish 17 barley linguine porter
porter 12 quesadilla barley
tuna 20 porter
There's no particular order in the file: tasks can be listed in any order, and the dependencies can be listed in any order on each line. There are no cycles in the dependencies: no task depends on a task which depends on it (directly or indirectly).

The example shows that the task quesadilla takes 18 minutes and barley takes 20 minutes. All told, these tasks will take you 139 minutes to complete them all.

Part 1
Given the instructions file in 04-preparation.txt, how long will it take you to complete all the tasks?
