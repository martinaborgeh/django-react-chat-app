import logo from './logo.svg';
import './App.css';
import { Route, Routes } from "react-router-dom";

import {Signup, Login} from './components/authentication'
import {CreateAppointment} from './components/create_appointment'
import {JoinMeeting} from './components/join_meeting'
import {ChatRoom} from './components/chatroom'
import {DoctorStartMeeting} from './components/startmeeting'






function App() {
  return (
    <div className="App">
      <Routes >
            <Route path="/signup" element={<Signup/>} />
            <Route path="/login" element={<Login/>} />
            <Route path="/startmeeting" element={<DoctorStartMeeting/>} />
            <Route path="/create-apppointment" element={<CreateAppointment/>} />
            <Route path="/join-meeting" element={<JoinMeeting/>} />
            <Route path="/chat-room" element={<ChatRoom/>} />

            
            
        </Routes>
    </div>
  );
}

export default App;
