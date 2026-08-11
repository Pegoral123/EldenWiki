const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("@/components/homePage.vue"),
  },
  {
    path: "/mainPage",
    name: "mainPage",
    component: () => import("@/components/mainPage.vue"),
    meta: { requiresAuth: true },
  },
  {
    path: "/LoginPage",
    name: "login",
    component: () => import("@/components/LoginPage.vue"),
  },
  {
    path: "/RegisterPage",
    name: "register",
    component: () => import("@/components/RegisterPage.vue"),
  },
];

export default routes;
