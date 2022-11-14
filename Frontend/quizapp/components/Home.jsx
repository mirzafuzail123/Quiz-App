import React from 'react'

export default function Home() {
  return (
    <>
      <div className='max-w-lg mx-auto min-h-screen'>
        <div className='flex p-4 '>
          <img src="https://high-8.com/assets/svg/crown.svg" alt="logo" width="24" height="24" /><span class="font-medium ml-2 text-secondary">High-8.Com</span>
        </div>

        <div className='text-center '>
          <img src="https://high-8.com/assets/svg/first.svg" class="mx-auto mb-10" />
          <h1 className='text-4xl text-secondary font-semibold'>How much your <br /><span className='zigzag'>friends</span> are </h1>
        </div>

        <div>
        <img src="https://high-8.com/assets/svg/home-banner.svg" alt="banner" width="250" height="155" class="w-full max-w-[250px] mt-6 mb-10 mx-auto"/>
        </div>
        <a href="/"><button className='text-white bg-primary rounded-full text-center w-full  font-medium py-5'>Create Quiz</button></a>
      </div>
    </>
  )
}
