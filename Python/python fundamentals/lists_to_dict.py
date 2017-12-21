def lists_to_dict(arr1,arr2):
    new_dict={}
    if len(arr1) == len(arr2):
        for i in range(len(arr1)):
            new_dict[arr1[i]]=arr2[i]
    # else:
    print new_dict





name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
lists_to_dict(name,favorite_animal)
