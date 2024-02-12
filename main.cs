using System;
namespace InputProgram
{
  class Program
  {
	static void Main (string[]args)
	{
	  string userName;
	    Console.Write ("Your Name:");
	    userName = Console.ReadLine ();
	    Console.WriteLine ("Hello " + userName);
	}
  }
}