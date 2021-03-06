n = int(input())
plates = list(map(int, input().split()))
clean = dirty = 0
isclean = True
for plate in plates:
    if plate == 1:
        # if isclean == True:
        #     clean -= 1
        #     dirty += 1
        dirty += 1
        isclean = False
    else:
        if isclean == False:
            dirty += 1
        else:
            clean += 1
            isclean = True
print("Clean:{}\nDirty:{}".format(clean, dirty))
        