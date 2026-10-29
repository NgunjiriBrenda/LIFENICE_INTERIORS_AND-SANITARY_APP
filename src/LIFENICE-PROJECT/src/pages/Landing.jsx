 import {Link} from "react-router-dom";

 const categories = [
    {

    name: "SPC Flooring",
    description: "Beautiful floors for modern living",
    image: "https://images.unsplash.com/photo-1655457397686-4dd23e78a918?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D",
    },
    
    {  
    name: "Wall Panels",
    description: "Beautiful floors for modern living",
    image: "https://images.unsplash.com/photo-1655457397686-4dd23e78a918?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D"

    },

    {
        name: "Marble Sheets",
        description: "Lightweight decorative panel",
        image: "https://i.pinimg.com/1200x/b5/f0/b8/b5f0b853c4bbc789bf6f8561ae8fba00.jpg",
    },

    {
        name: "PU Stones",
        description: "Decorative wall panel",
        image: "https://i.pinimg.com/736x/1a/be/62/1abe62023a00eac931e36ac5568c1cf5.jpg",
    },

    {
        name: "Cornices",
        description: "Decorative bridging wall and ceiling",
        image: "https://i.pinimg.com/736x/8c/1c/1a/8c1c1aaebd5a9ff26e8a09f91d7498be.jpg",

    },

    {
        name: "Wainscoting",
        description: "Traditional style of panel",
        image: "https://i.pinimg.com/736x/fc/2b/50/fc2b502cf471f590428bbef2265e4967.jpg",
    },
 ];
 export default function Landing(){
    return (
        <div className="min-h-screen bg-stone-50 text-stone-900">
        
        <header className="border-b border-stone-200 bg-white">
            <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-5">
                <Link to="/"className="text-2xl font-bold tracking-tight">
                Life<span className="text-amber-800">Nice.</span>
                </Link>

                <div className="hidden items-center gap-8 md:flex">
                    <Link to="/"className="hover:text-amber-800">Home </Link>
                    <Link to="/proucts"className="hover:text-amber-800">Products </Link>
                    <Link to="/login"className="hover:text-amber-800">Login</Link>

                </div>

                <Link to="/products"className="rounded-full bg-amber-900 px-5 py-3 text-sm font-semibold text-white transition hover:bg-amber-800">
                Shop now
                </Link>

                </nav>

                </header>

                <main>
                    <section className="mx-auto grid max-w-7xl items-center gap-10 px-6 py-16 md:grid-cols-2 md:py-24">
                        <div>
                            <p className="mb-5 text-sm font-semibold uppercase tracking-[0.25em]text-amber-800">
                                Thoughtful spaces.Beautiful living </p>

                            <h1 className="max-w-xl text-5xl font-bold leading-tight tracking-tight md:text-7xl">
                                Make your space feel like{" "}<span className="text-amber-800">home</span> </h1>

                            <p className="mt-6 max-w-lg text-lg leading-8 text-stone-600">
                                Discover stylish flooring, elegant wall panels and bathroom essentials designed to bring your interior dreams to life</p>

                            <div className="mt-8 flex flex-wrap gap-4">
                                <Link to="/products"className="rounded-full bg-amber-900 px-7 py-4 font-semibold text-white transition hover:bg-amber-800">
                                Explore products </Link>

                            <a href="#categories"className="round-full border border-stone-300 px-7 py-4 font-semibold transition hover:bg-stone-100">
                                Discover more
                            </a>

                            </div>

                            <p className="mt-8 text-sm text-stone-500">
                                Flooring Wall Panel Bathroom essentials </p>
                            </div>

                            <div className="relative">

                                <img src="https://plus.unsplash.com/premium_photo-1661963201626-2c69cfbe4f8a?w=400&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=NHwxMjA3fDA%3D" alt="Elegant modern living room interior"
                                className="h-[360px] w-full rounded-3xl object-cover shadow-xl md:h-[520px]"/>

                                <div classname="absolute -bottom-5 left-4 rounded-2xl bg-white p-5 shadow-lg sm:left-8">

                                    <p className="text-sm text-stone-500">Your space, your style</p>

                                    <p classname="mt-1 font-bold">Designed for better living.</p>

                                </div>
                            </div>
                        </section>

                        <section id="categories"className="bg-white py-20">
                            <div className="mx-auto max-w-7xl px-6">
                                <div className="mb-10 flex flex-wrap items-end justify-between gap-4">
                                    <div>
                                        <p className="text-sm font-semibold uppercase tracking-widest text-amber-800">
                                            Explore our collection
                                        </p>
                                        <h2 className="mt-3 text-3xl font-bold md:text-4xl">Find your interior style</h2>
                                        
                                    </div>

                                    <Link to="/products"className="font-semibold text-amber-900 hover:underline">View all products</Link>

                                    </div>

                                    <div className="grid gap-7 sm:grid-cols-2 lg:grid-cols-3">{categories.map((category) =>(
                                        <Link to="/products" key={category.name}className="group overflow-hidden rounded-2xl border border-stone-100 bg-stone-50 transition hover:-translate-y-1 hover:shadow-lg">
                                            <mg src={category.image} alt={category.name}className="h-64 w-full object-cover transition duration-500 group-hover:scale-105"/>

                                            <div className="px-6">

                                                <h3 className="text-xl font-bold">{category.name}</h3>
                                                <p className="mt-2 text-stone-600">{category.description}</p>
                                                <p className="mt-4 font-semibold text-amber-900">Explore collection</p>
                                            </div>
                                        </Link>
                                    ))}
                                    </div>
                                    
                                </div>
                        </section>

                        <section className="bg-amber-950 px-6 py-16 text-center text-wite md:py-20">
                            <h2 className="text-3xl font-bold md:text-4xl">Ready to transform your space?</h2>

                            <p className="mx-auto mt-4 max-w-xl leading-7 text-amber-100">
                                Discover interior essentials that bring comfort, style and personality into every room.
                            </p>
                            <Link to="/products" className="mt-8 incline-block rounded-full bg-white px-7 py-4 font-semibold text-amber-950 transition hover:bg-amber-100">
                            Start exploring
                            </Link>

                        </section>


                </main>

                <footer className="bg-stone-100 px-6 py-8 text-center text-sm text-stone-600">
                    {new Date().getFullYear()} LifeNice Interiors.All rights reserved.
                    
                </footer>

                </div>
    );
 }

