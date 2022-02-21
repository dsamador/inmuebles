import { Component, OnInit } from '@angular/core';
import { AngularFirestore } from '@angular/fire/compat/firestore';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit{
  title = 'mi-web-app';
  /**
   *
   */
  constructor(private fs : AngularFirestore) {

  }

  ngOnInit(): void {
      this.fs.collection('test').stateChanges().subscribe(
        personas => {console.log(personas.map(
          p=>p.payload.doc.data()
        ))}
      );
  }
}
