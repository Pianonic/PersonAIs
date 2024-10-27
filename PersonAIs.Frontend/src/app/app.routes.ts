import { Routes } from '@angular/router';
import { GeneratePersonaComponent } from './generate-persona/generate-persona.component';
import { SettingsComponent } from './settings/settings.component';
import { ProfileComponent } from './profile/profile.component';
import { ProjectsComponent } from './projects/projects.component';

export const routes: Routes = [
    { path: '', component: ProjectsComponent }, // Default route
    { path: 'generate-persona', component: GeneratePersonaComponent },
    { path: 'settings', component: SettingsComponent },
    { path: 'profile', component: ProfileComponent },
    { path: '**', redirectTo: '' } // Redirect to home for unknown routes
  ];