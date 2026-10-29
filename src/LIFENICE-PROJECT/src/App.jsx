import {BrowserRouter, Routes, Route} from "react-router-dom";
import Landing from "./pages/Landing";

function ComingSoon({page}) {
  return (
    <main className="min-h-screen bg-stone-50 p-10 text-center">
      <h1 className="text-3xl font-bold text-amber-900">{page}</h1>
      <p className="mt-4 text-stone-600">This page is coming soon.Let's build it next!</p>
    </main>
  );
}

export default function App(){
  return (
    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/products"element={<ComingSoon page="Products" />}/>
      <Route path="/login" element={<ComingSoon page="Login" />} />
      <Route path="/sign-up" element={<ComingSoon page="Sign Up" />} />
      <Route path="/product/:id" element={<ComingSoon page="Product Details"/>}/>
      <Route path="/cart" element={<ComingSoon page="Shopping Cart"/>}/>
      <Route path="/checkout"element={<ComingSoon page="Checkout"/>}/>
      <Route path="/admin" element={<ComingSoon page="Admin Dashboard"/>} />

    </Routes>

    </BrowserRouter>

      
  )
}
