import { Card } from 'react-bootstrap';
import { ProfileInterface } from '../interfaces/ProfileInterface';

function ProfileCard(props: ProfileInterface) {
    return (
        <Card bg='success' className='shadow border-0 py-1' style={{ maxHeight: "225px", borderRadius: 13 }}>
            <Card.Header className='border-0 p-1'>
                <div className='d-flex'>
                    <div className='d-flex justify-content-center align-items-center p-2'>
                        <img src={props.image as string} alt="" height={90} width={90} className="bg-dark" style={{ borderRadius: 50, objectFit: "cover" }} />
                    </div>
                    <div className='w-100 p-2 text-truncate' >
                        <div className='h-50 w-100 d-flex align-items-end text-truncate align-middle'>
                            <p className='text-white m-0 fs-4 fw-bolder text-truncate'>
                                {props.nom}
                            </p>
                        </div>
                        <div className='h-50 w-100 d-flex align-items-start'>
                            <p className='text-white m-0 fs-4 fw-bold text-truncate'>
                                {props.prenom}
                            </p>
                        </div>
                    </div>
                </div>
                <div className='' >
                    <div className='w-100 text-truncate' >
                        <div className='w-100 px-2 d-flex align-items-end text-truncate align-middle'>
                            <p className='text-white m-0 mx-1 fs-5 fw-semibold text-truncate'>
                                Tél: {props.tel}
                            </p>
                        </div>
                        <div className='w-100 px-2 d-flex align-items-center'>
                            <p className='text-white m-0 mx-1 fs-5 fw-semibold text-truncate'>
                                Email: {props.email}
                            </p>
                        </div>
                        <div className='d-flex px-2 align-items-center'>
                            <p className='text-white m-1 fs-5 fw-semibold text-truncate'>
                                <i className="pe-1 bi-linkedin"></i>
                            </p>
                            <p className='m-1 fs-5 fw-semibold text-truncate'>
                                <i className="text-white px-1 bi-github"></i>
                            </p>
                            <p className='m-1 fs-5 fw-semibold text-truncate'>
                                <i className="text-white px-1 bi-bootstrap"></i>
                            </p>
                        </div>
                    </div>
                </div>
            </Card.Header>
        </Card>
    );
  }
  
  export default ProfileCard;