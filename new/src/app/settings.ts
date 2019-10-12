interface Settings {
  production: boolean;
  APIurl: string;
  domain: string;
}

import {InjectionToken} from '@angular/core';

export const APP_CONFIG = new InjectionToken<SettingClass>('APP_CONFIG');


export class SettingClass implements Settings {
  production: boolean=  false;
  APIurl: string = 'https://ng-dating-test.webmonstr.com';
  domain: string = 'https://ng-dating-test.webmonstr.com';
}
import { SocketIoConfig } from 'ngx-socket-io';
export const SOCKET_CONFIG: SocketIoConfig = { url: 'https://ng-dating-test.webmonstr.com:8888', options: {path:'/websocket'} };

import {HttpClient} from '@angular/common/http';
import {TranslateHttpLoader} from '@ngx-translate/http-loader';
import { HttpClientModule } from '@angular/common/http';

export function HttpLoaderFactory(http: HttpClient) {
  return new TranslateHttpLoader(http, 'https://ng-dating-test.webmonstr.com/i18n/', '.json');
}
