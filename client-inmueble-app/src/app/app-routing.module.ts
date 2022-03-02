import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: ''
    ,children: [
      {
        path: 'static'
        ,loadChildren: () => import('./pages/static/static.module').then(m=>m.StaticModule)
      },
      {
        path:''
        ,pathMatch: 'full'
        ,redirectTo: 'static/welcome'
      }
    ]
  },
  {//ruta para ruta no encontrada
    path: '**'
    ,pathMatch: 'full'
    ,redirectTo: 'static/welcome'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
