const routes = [
  {
    path: "/",
    component: () => import("@/components/homePage.vue"),
  },
  {
    path: "/mainPage",
    component: () => import("@/components/mainPage.vue"),
  },
  {
    path: "/LoginPage",
    component: () => import("@/components/LoginPage.vue"),
  },
  {
    path: "/RegisterPage",
    component: () => import("@/components/RegisterPage.vue"),
  },
];

export default routes;
