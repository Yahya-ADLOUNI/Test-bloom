import './App.css';
import ProfileCard from './components/ProfileCard';
import { ProfileInterface } from './interfaces/ProfileInterface';
import image from "./image.png";

function App() {

  const cards = [
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
    {
      nom: "NOM",
      prenom: "Prénom",
      tel: "06 00 00 00 00",
      email: "email@email.io",
      image: image
    },
  ]


  return (
    <div className="css-full-screen bg-white container shadow-lg" style={{ overflow: "hidden", padding: "1vh" }}>
      <div className='row d-flex row-cols-1 row-cols-sm-1 row-cols-md-2 row-cols-xl-3 row-cols-xxl-3 m-0 py-2' style={{ overflowY: "auto", maxHeight: "96vh" }}>
        {
          cards?.map((value: ProfileInterface, index: number) => {
            return(
              <div key={index} className='col m-0 pb-3'>
                <ProfileCard {...value} />
              </div>
            );
          })
        }
        {
          cards?.map((value: ProfileInterface, index: number) => {
            return(
              <div key={index} className='col m-0 pb-2'>
                <ProfileCard {...value} />
              </div>
            );
          })
        }
      </div>
    </div>
  );
}

export default App;