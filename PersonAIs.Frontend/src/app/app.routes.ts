import { Routes } from '@angular/router';
import { GeneratePersonaComponent } from './generate-persona/generate-persona.component';
import { ProfileComponent } from './profile/profile.component';
import { ProjectsComponent } from './projects/projects.component';

export const routes: Routes = [
    { path: 'projects', component: ProjectsComponent },
    { path: 'generate-persona', component: GeneratePersonaComponent },
    { path: 'profile', component: ProfileComponent },
    { path: '**', redirectTo: '' }
  ];