import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router, NavigationEnd } from "@angular/router";
declare var jQuery: any;

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css'],
  providers: [UserService]

})
export class MainComponent implements OnInit {


  input;
  loggedIn=false
  constructor(private userservice:UserService, 
    private router:Router) {}

  ngOnInit(){

    (function ($) {    
      $(document).ready(function() {
        var modal = document.getElementById('login-form');
        window.onclick = function(event) 
        {
            if (event.target == modal) 
            {
                modal.style.display = "none";
            }
        }  
  })
})(jQuery);
  




    this.input={
      username:'',
      password:'',
      
    };
  }
  onLogin(){
    this.userservice.loginUser(this.input).subscribe(
      Response => {
        console.log("response sucessfully",Response)
        this.loggedIn=true
        this.router.navigate(['home'])
      },
      error => {

        console.log('error',error,this.input)
        alert('invaild Password or Id')
        
      
      }
      );
  }


  onRegister(){
    this.userservice.registerNewUser(this.input).subscribe(
      Response => {
        alert('user' +  this.input.username + 'has been created')
      },
      error => console.log('error',error)
    );
  }

}
