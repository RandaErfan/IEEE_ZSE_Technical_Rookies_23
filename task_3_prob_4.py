def num_of_turns(pages,page_wanted):
    if pages % 2 == 0:
        pages+=1
    return min((page_wanted+1)/2,(pages-page_wanted-1)/2)
pages = int(input("number of pages :"))
page_wanted = int(input())
num_of_turns(pages ,page_wanted)
