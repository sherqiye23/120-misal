#59cu sual
#N-rəqəmli ədəd daxil edin. Bu ədədin yazılışında ən çox təkrarlanan rəqəmi təyin edin.
n=list(input(' Ədəd yazın: '))
list=[n.count('0'),n.count('1'),n.count('2'),n.count('3'),n.count('4'),n.count('5'),n.count('6'),n.count('7'),n.count('8'),n.count('9')]

print(' Ən çox təkrarlanan:',list.index(max(list)))