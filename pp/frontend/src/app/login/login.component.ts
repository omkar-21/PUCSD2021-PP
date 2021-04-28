import { Component, OnInit } from '@angular/core';
import { ViewEncapsulation } from '@angular/core';
import { HomeService } from 'src/app/login/home.service';
import { Router, NavigationEnd } from "@angular/router";
import {ConfirmationService} from 'primeng/api';
import {MessageService} from 'primeng/api';
declare var jQuery: any;

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private homeservice:HomeService,private confirmationService: ConfirmationService, 
    private messageService: MessageService, private router:Router) {}
    latestnews;
    latestexam;
    input;
    ngOnInit(): void {
    (function ($) {
    $(document).ready(function(){
      // Add smooth scrolling to all links
      $("a").on('click', function(event) {
    
        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {
          // Prevent default anchor click behavior
          event.preventDefault();
    
          // Store hash
          var hash = this.hash;
    
          // Using jQuery's animate() method to add smooth page scroll
          // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 800, function(){
    
            // Add hash (#) to URL when done scrolling (default click behavior)
            window.location.hash = hash;
          });
        } // End if
      });
    });
  })(jQuery);
  (function ($) {    
    $(document).ready(function() {
      var stickyNavTop = $('.nav').offset().top;
    
      var stickyNav = function(){
        var scrollTop = $(window).scrollTop();
    
        if (scrollTop > stickyNavTop) { 
          $('.nav').addClass('sticky');
        } else {
          $('.nav').removeClass('sticky'); 
        }
      };
    
      stickyNav();
    
      $(window).scroll(function() {
        stickyNav();
      });
    });

})(jQuery);


this.homeservice.latestexam().subscribe(
  Response => {
    this.latestexam=[Response.data['name']]
  },
  error => console.log('error',error)
);

this.homeservice.latestnews().subscribe(
  Response => {
    this.latestnews=[Response.data['heading']]

    console.log("news",this.latestnews[0]);

  },
  error => console.log('error',error)
);
this.input={
  email_id:'',
  mobile_no:'',
  
};

}

  images=["../../assets/college2.jpeg","../../assets/exam2.jpg","../../assets/news2.jpg","../../assets/slider-image1.jpg","../../assets/slider-image2.jpg","../../assets/slider-image3.jpg"];
isCollapsed="true";

confirm() {
  this.confirmationService.confirm({
      message: 'Are you sure that you want to perform this action?',
      accept: () => {
        this.homeservice.activateMsgService(this.input).subscribe(
          Response => {
            this.messageService.add({severity:'success', summary:'Service Message', detail:'Via MessageService'});
          },
          error => console.log('error',error)
        );

      }
  });
}

logout(){
  this.homeservice.logoutUser(this.input).subscribe(
    Response => {
      this.router.navigate([''])
    },
    error => console.log('error',error)
  );
}

}
