namespace DAL
{
    public interface IUOW
    {
        void Dispose(bool disposing);
        void Dispose();
        void Save();
    }
}