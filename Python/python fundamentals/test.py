# dict1 = {"name":"yangLuo","age":"26", "gender":"male"}
# value =["mickey",100, "female"]
# # print dict.items()
# # print dict.iteritems()
# dict2 = dict.fromkeys(dict1,element for element in value)
# print dict2

class User(object):
      name = "Anna"


anna = User()
print "anna's name: ", anna.name
User.name = "Bob"
print "anna's name after change:", anna.name
bob = User()
print "bob's name:", bob.name

class Program
{
    public static void SayHello( string name = "ekko")
    {
        Console.WriteLine($"Hello, this is {name}");
    }
    public void Main(string[] args)
    {
        SayHello(); # call static functioin within declared class directly
    }
}
class Program
{
    public  void SayHello( string name = "ekko")
    {
        Console.WriteLine($"Hello, this is {name}");
    }
    public void Main(string[] args)
    {
        Program program = new Program(); # new object/instance needed to call non-static function
        program.SayHello();
    }
}
