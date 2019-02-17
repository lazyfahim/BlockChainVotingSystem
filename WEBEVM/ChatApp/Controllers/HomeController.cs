using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using DAL;
using Microsoft.Owin.Security.Facebook;
using Model;
using AppContext = DAL.AppContext;

namespace ChatApp.Controllers
{
    public class HomeController : Controller
    {
        public UOW unit;
        public HomeController()
        {
            unit = new UOW(new AppContext());
        }
        public ActionResult Index()
        {
            var elections = unit.ElectionRepository.Get();
            return View(elections);
        }

        public ActionResult Details(Guid Id)
        {
            var election = unit.ElectionRepository.GetById(Id);
            return View(election);
        }

        public ActionResult Voting(Guid Id)
        {
            var election = unit.ElectionRepository.GetById(Id);
            return View(election);
        }
        [HttpGet]
        public ActionResult Create()
        {
            return View();
        }
        [HttpPost]
        public ActionResult Create(Election election)
        {
            election.Id = Guid.NewGuid();
            unit.ElectionRepository.Insert(election);
            unit.Save();
            return View();
        }
        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }
    }
}