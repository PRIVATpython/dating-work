import { Component, OnInit, Inject, TemplateRef } from '@angular/core';
import {TranslateService} from '@ngx-translate/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {


  constructor(
    private translate: TranslateService,
    ) {
      translate.setDefaultLang('en');
    }

  ngOnInit() {



  }




}
