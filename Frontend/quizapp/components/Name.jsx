import React from 'react'

export default function Name() {
    return (
        <div className='max-w-lg mx-auto min-h-screen ' style={{backgroundColor:'whitesmoke'}}>
            <div className='flex p-4 mb-10'>
                <img src="https://high-8.com/assets/svg/crown.svg" alt="logo" width="24" height="24" /><span className="font-medium ml-2 text-secondary">High-8.Com</span>
            </div>
            <div className='text-center mb-10 '>
                <h1 className='p-5 text-4xl font-semibold text-secondary mt-10'>What's your <span className='zigzag'>Name</span>?</h1>
            </div>
            <div className='m'>
            <input type="text" name='username' id='username' placeholder='your name...' className='rounded-full w-full focus:ring' />

            </div>
        </div>
    )
}
