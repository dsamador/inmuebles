import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

/* FIREBASE */

import {AngularFireModule} from '@angular/fire/compat';
import {AngularFireStorageModule} from '@angular/fire/compat/storage';
import {AngularFirestoreModule} from '@angular/fire/compat/firestore';
import {AngularFireAuthModule} from '@angular/fire/compat/auth';

import { provideFirebaseApp, initializeApp } from '@angular/fire/app';
import {getFirestore, provideFirestore} from '@angular/fire/firestore';
import {getAuth, provideAuth} from '@angular/fire/auth';
import {getStorage, provideStorage} from '@angular/fire/storage';

/* END FIREBASE */

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { environment } from '@src/environments/environment';
import { IndicatorsModule } from './shared/indicators/indicators.module';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { PopupsModule } from './shared/popups/popups.module';

import { NotificationModule } from './services';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule

    ,provideFirebaseApp(
      ()=>initializeApp(environment.firebase.config))
    ,provideFirestore(()=>getFirestore())
    ,provideStorage(()=>getStorage())
    ,provideAuth(()=>getAuth())
    ,AngularFireModule.initializeApp(environment.firebase.config)
    ,AngularFireStorageModule
    ,AngularFirestoreModule
    ,AngularFireAuthModule

    ,IndicatorsModule
    ,BrowserAnimationsModule
    ,PopupsModule
    ,NotificationModule.foRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
